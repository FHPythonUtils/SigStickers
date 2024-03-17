import json
from pathlib import Path

from sigstickers.caching import CACHE_DIR, create_converted, verify_converted

THISDIR = Path(__file__).resolve().parent


# just want files that exist here
file_exists = "pyproject.toml"
file_exists_2 = ".gitignore"


def test_verify_converted_v1():
	pack_name = "Test_Pack_v1"
	cache_file = CACHE_DIR / pack_name
	cache_data = {
		"info": {"swd": f"{THISDIR}/data"},
		"converted": {"converted": 10, "total": 10},
	}
	cache_file.write_text(json.dumps(cache_data))

	assert verify_converted(Path(pack_name))


def test_verify_converted_v2():
	pack_name = "Test_Pack_v2"
	cache_file = CACHE_DIR / pack_name
	cache_data = {
		"version": 2,
		"webp_files": [file_exists, file_exists_2],
		"converted_files": [[file_exists], [file_exists_2]],
	}
	cache_file.write_text(json.dumps(cache_data))

	assert verify_converted(Path(pack_name))


def test_create_converted():
	pack_name = "Test_Pack"
	cache_data = {"example_key": "example_value"}

	create_converted(Path(pack_name), cache_data)

	cache_file = CACHE_DIR / pack_name
	assert cache_file.exists()
	assert json.loads(cache_file.read_text()) == cache_data
