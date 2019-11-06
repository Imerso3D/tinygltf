from conans import ConanFile

class TinyGLTFConan(ConanFile):
    name = "tinygltf"
    version = "2.2.0"
    exports_sources = "tiny_gltf.h"
    no_copy_source = True
    requires = (
        "stb/20190512@conan/stable",
        "jsonformoderncpp/3.6.1@vthiery/stable",
    )

    def package(self):
        self.copy("*.h", dst="include/tinygltf/")