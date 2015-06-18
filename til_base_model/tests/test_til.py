# -*- coding:utf-8 -*-

from til_base_model.tests.base import create_til_simulation, plot_population2

simulation = create_til_simulation(capitalized_name = 'Patrimoine_next_200', uniform_weight = 200)
simulation.run()
plot_population2(simulation)
