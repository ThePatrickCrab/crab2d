#include "Engine.hpp"

#include <chrono>
#include <iostream>
#include <thread>

Engine::Engine()
{
	std::cout << "Creating Engine..." << std::endl;
}

void Engine::Start()
{
	std::cout << "Starting Engine." << std::endl;
	for(unsigned i = 0; i < 10; i++)
	{
		std::cout << i << ' ' << std::flush;
		std::this_thread::sleep_for(std::chrono::milliseconds(500));
	}
	std::cout << "\nFinished." << std::endl;
}
