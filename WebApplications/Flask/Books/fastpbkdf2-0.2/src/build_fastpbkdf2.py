# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

import os

import sys

import tarfile

import tempfile

from cffi import FFI


TAR_FILE = os.path.join(os.path.dirname(__file__), "fastpbkdf2.tar.gz")
DIR = tempfile.mkdtemp()

with tarfile.open(TAR_FILE) as f:
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(f, DIR)
    DIR = os.path.join(DIR, f.getmembers()[0].name)


def _get_openssl_libraries(platform):
    if platform == "win32":
        return ["libeay32", "crypt32", "advapi32",
                "gdi32", "user32", "ws2_32"], ["/O2", "/WX", "/nologo"]
    else:
        return ["crypto"], ["-std=c99", "-O3", "-g"]


lib, compile_args = _get_openssl_libraries(sys.platform)

ffi = FFI()
ffi.cdef(
    """
    void fastpbkdf2_hmac_sha1(const uint8_t *, size_t,
                              const uint8_t *, size_t,
                              uint32_t,
                              uint8_t *, size_t);

    void fastpbkdf2_hmac_sha256(const uint8_t *, size_t,
                                const uint8_t *, size_t,
                                uint32_t,
                                uint8_t *, size_t);

    void fastpbkdf2_hmac_sha512(const uint8_t *, size_t,
                                const uint8_t *, size_t,
                                uint32_t,
                                uint8_t *, size_t);
    """
)

ffi.set_source(
    "_fastpbkdf2",
    """
    #include "fastpbkdf2.h"
    """,
    sources=[
        os.path.join(DIR, "fastpbkdf2.c"),
    ],
    include_dirs=[DIR],
    libraries=lib,
    extra_compile_args=compile_args
)
