from conans import ConanFile


class FooConan(ConanFile):
    name = "foo"
    version = "0.1.0"
    exports_sources = "sample.txt"

    def package(self):
        self.copy("sample.txt", dst="res")
