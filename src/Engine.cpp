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
	std::chrono::time_point tp =
	    std::chrono::steady_clock::now() + std::chrono::milliseconds(500);
	for(unsigned i = 0; i < 10; i++)
	{
		std::cout << i << ' ' << std::flush;
		if(i == 3)
		{
			std::this_thread::sleep_for(std::chrono::milliseconds(2000));
		}
		std::this_thread::sleep_until(tp);
		tp += std::chrono::milliseconds(500);
	}
	std::cout << "\nFinished." << std::endl;
}
