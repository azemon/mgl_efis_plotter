from mgl_efis_plotter import *

config = Config()
flights = create_flights('IEFIS.REC', config)
p = Plot(flights[0])
p.plot2(['pAltitude', 'densityAltitude', 'oat']).show()