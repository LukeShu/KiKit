
.SHELLFLAGS += -e

PCM_KIKIT_RESOURCES := $(shell find pcm/kikit -type f -print) \
	$(shell find kikit/resources/graphics -type f -print)
PCM_LIB_RESOURCES :=  $(shell find pcm/kikit-lib -type f -print) \
	$(shell find kikit/resources/graphics -type f -print) \
	$(shell find kikit/resources/kikit.kicad_sym -type f -print) \
	$(shell find kikit/resources/kikit.pretty -type f -print)

.PHONY: doc clean package release test test-system test-unit docker-release

all: doc package test pcm

doc: docs/panelization/python_api.md docs/panelization/examples.md

docs/panelization/python_api.md: kikit/panelize.py scripts/panelizeDoc.py
	PYTHONPATH="$(pwd):${PYTHONPATH}" python3 scripts/panelizeDoc.py > $@

doc/resources/conn.png: docs/resources/conn.kicad_pcb
	pcbdraw plot --silent $< $@
	convert $@ -define png:include-chunk=none $@

docs/panelization/examples.md: scripts/exampleDoc.py docs/resources/conn.png
	PYTHONPATH="$(pwd):${PYTHONPATH}" python3 scripts/exampleDoc.py > $@

package:
	rm -f dist/*
	python3 -m build

install: package
	pip3 install --no-deps --force dist/*.whl

release: package
	twine upload dist/*

test: test-system test-unit

test-system: build/test $(shell find kikit -type f)
	cd build/test && bats ../../test/system

test-unit:
	cd test/units && pytest

build/test:
	mkdir -p $@

pcm: pcm-kikit pcm-lib

pcm-kikit: $(PCM_KIKIT_RESOURCES)
	rm -rf build/pcm-kikit build/pcm-kikit.zip
	mkdir -p build/pcm-kikit
	mkdir -p build/pcm-kikit/resources
	cp -r pcm/kikit/* build/pcm-kikit
	find build/pcm-kikit -name "*.pyc" -type f -delete
	cp kikit/resources/graphics/kikitIcon_64x64.png build/pcm-kikit/resources/icon.png
	ls -lah build
	scripts/setJson.py -s versions.-1.install_size=$$( find build/pcm-kikit -type f -exec ls -la {} + | tr -s ' ' | cut -f5 -d' ' | paste -s -d+ - | bc ) \
		build/pcm-kikit/metadata.json build/pcm-kikit/metadata.json
	cd build/pcm-kikit && zip ../pcm-kikit.zip -r *
	cp build/pcm-kikit/metadata.json build/pcm-kikit-metadata.json
	scripts/setJson.py \
		-s versions.-1.download_sha256=\"$$( sha256sum build/pcm-kikit.zip | cut -d' ' -f1)\" \
		-s versions.-1.download_size=$$( du -sb build/pcm-kikit.zip | cut -f1) \
		-s versions.-1.download_url=\"TBA\" \
		build/pcm-kikit-metadata.json build/pcm-kikit-metadata.json

pcm-lib: $(PCM_LIB_RESOURCES)
	rm -rf build/pcm-kikit-lib build/pcm-kikit-lib.zip
	mkdir -p build/pcm-kikit-lib
	mkdir -p build/pcm-kikit-lib/resources
	mkdir -p build/pcm-kikit-lib/symbols
	mkdir -p build/pcm-kikit-lib/footprints
	cp -r pcm/kikit-lib/* build/pcm-kikit-lib
	cp kikit/resources/graphics/kikitIcon_64x64.png build/pcm-kikit-lib/resources/icon.png
	cp -r kikit/resources/kikit.pretty build/pcm-kikit-lib/footprints
	cp -r kikit/resources/kikit.kicad_sym build/pcm-kikit-lib/symbols
	scripts/setJson.py -s versions.-1.install_size=$$(find build/pcm-kikit-lib -type f -exec ls -la {} + | tr -s ' ' | cut -f5 -d' ' | paste -s -d+ - | bc) \
		build/pcm-kikit-lib/metadata.json build/pcm-kikit-lib/metadata.json
	cd build/pcm-kikit-lib && zip ../pcm-kikit-lib.zip -r *
	cp build/pcm-kikit-lib/metadata.json build/pcm-kikit-lib-metadata.json
	scripts/setJson.py \
		-s versions.-1.download_sha256=\"$$( sha256sum build/pcm-kikit-lib.zip | cut -d' ' -f1)\" \
		-s versions.-1.download_size=$$( du -sb build/pcm-kikit-lib.zip | cut -f1) \
		-s versions.-1.download_url=\"TBA\" \
		build/pcm-kikit-lib-metadata.json build/pcm-kikit-lib-metadata.json

docker-release:
	docker build -t yaqwsx/kikit:$(shell git describe --tags --always)-KiCAD8 --build-arg="KICAD_VERSION=8.0" .
	docker build -t yaqwsx/kikit:latest --build-arg="KICAD_VERSION=8.0" .
	docker build -t yaqwsx/kikit:$(shell git describe --tags --always)-KiCAD7 --build-arg="KICAD_VERSION=7.0" .

clean:
	rm -rf dist build

# Manually link in system pcbnew+wx, instead of using
# `--system-site-packages`, to have maximum isolation from the host
# Python.  Notably, system `mypy` won't find packages in the venv.
_empty :=
_space := $(_empty) $(_empty)
_STD_PATH := $(subst $(_space),:,$(filter-out $(CURDIR)/venv/bin,$(subst :,$(_space),$(PATH))))
stdpython3 = PATH=$(_STD_PATH); unset VIRTUAL_ENV; python3
venv: pyproject.toml setup.py
	python3 -m venv $@
	ln -sf "$$($(stdpython3) -c 'import _pcbnew; print(_pcbnew.__file__)')"     $@/lib/python*/site-packages/
	ln -sf "$$($(stdpython3) -c 'import pcbnew; print(pcbnew.__file__)')"       $@/lib/python*/site-packages/
	ln -sf "$$($(stdpython3) -c 'import wx; print(wx.__path__[0])')"{,Python-*} $@/lib/python*/site-packages/
	$@/bin/pip install setuptools
	$@/bin/pip install -e '.[dev]'
# SolidPython==1.1.3 is broken with setuptools>=82.  The fix is in Git
# master, but at this time 1.1.4 hasn't been released yet.  If this is
# the case, upgrade to a Git version.  Distros shipping both
# setuptools>=82 and SolidPython (eg: Arch Linux) either do this, or
# backport the fix to 1.1.3.
	if $@/bin/python -c 'import sys;exec("try:\n\timport solid\nexcept ModuleNotFoundError as e:\n\tif e.name == \"pkg_resources\":\n\t\tsys.exit(0)");sys.exit(1)'; then \
		$@/bin/pip install 'solidpython @ git+https://github.com/SolidCode/SolidPython@dcee03e9350a2309ee2fc191b46acf4a00199aff'; \
	fi
	$@/bin/pip install pcbdraw
	touch --no-create $@

py_sources = $(shell git ls-files :*.py :!kikit/_version.py :!versioneer.py)
pyi_sources = $(shell git ls-files :*.pyi)

format:
	black $(py_sources) $(pyi_sources)
	isort $(py_sources) $(pyi_sources)
check-format:
	black --check $(py_sources) $(pyi_sources)
	isort --check $(py_sources) $(pyi_sources)
.PHONY: format check-format

mypy_env = MYPYPATH=$(CURDIR)/mypy-stubs
mypy_env += PYTHONPATH=.$(if $(PYTHONPATH),:$(PYTHONPATH))

mypy_flags = --strict
#mypy_flags += --no-incremental --verbose

mypy_py_sources = setup.py
mypy_py_sources += kikit/__init__.py
mypy_py_sources += kikit/typing.py
mypy_py_sources += kikit/intervals.py
mypy_py_sources += kikit/units.py
mypy_py_sources += kikit/defs.py
mypy_py_sources += kikit/sexpr.py

mypy_py_sources += test/units/__init__.py
mypy_py_sources += test/units/test_intervals.py
mypy_py_sources += test/units/test_units.py
mypy_py_sources += test/units/test_sexpr.py

mypy_py_sources += kikit/doc.py
mypy_py_sources += scripts/exampleDoc.py
mypy_py_sources += scripts/exampleScripting.py
mypy_py_sources += scripts/panelizeDoc.py
mypy_py_sources += scripts/setJson.py

mypy:
	$(mypy_env) mypy $(mypy_flags) $(mypy_py_sources) $(pyi_sources)
.PHONY: mypy
