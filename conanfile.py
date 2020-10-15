'''
Conan file docs: https://docs.conan.io/en/latest/reference/conanfile.html
'''

from conans import ConanFile, CMake, tools

class Crab2d(ConanFile):
	name = 'crab2d'
	license = 'MIT'
	author = 'Patrick Crabtree <pconnorcrabtree@gmail.com>'
	url = 'https://github.com/ThePatrickCrab/crab2d'
	description = 'A simple 2D game engine.'
	settings = 'os', 'compiler', 'build_type', 'arch'
	options = {'build_testing': [True, False]}
	default_options = 'build_testing=True', 'sfml:graphics=True', 'sfml:window=True'
	generators = 'cmake'
	exports_sources = 'CMakeLists.txt', 'include/*', 'src/*'
	requires = 'sfml/2.5.1@bincrafters/stable'

	def set_version(self):
		git = tools.Git(folder=self.recipe_folder)
		# if not git.is_pristine():
		# 	raise ConanException("Please commit changes before creating/installing this package.")

		self.output.info(f'''\
Type: {type(git.get_tag())}
Value: {git.get_tag()}
''')
		version = '0.0.0'
		# tag = git.get_tag()
		# if tag is not None:
		# 	self.version = f'{version}_{git.get_revision()}'
		# else:
		self.version = f'{version}_{git.get_revision()[:7]}'

	def is_testing(self):
		return self.options.build_testing

	def build_requirements(self):
		if self.is_testing():
			self.build_requires('gtest/1.8.1')

	def _configure_cmake(self):
		cmake = CMake(self)

		cmake.definitions['CONAN_SPECIFIED_VERSION'] = f'{self.version}'
		if not self.is_testing():
			cmake.definitions["BUILD_TESTING"] = "NO"

		cmake.configure()
		return cmake

	def build(self):
		cmake = self._configure_cmake()
		cmake.build()
		if self.is_testing():
			cmake.test(output_on_failure=True)

	def package(self):
		cmake = self._configure_cmake()
		cmake.install()

	def depoly(self):
		# TODO: how is this different than package?
		pass
