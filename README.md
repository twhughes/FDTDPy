FDTDPy
======

(Currently) 1D FDTD solver and real time visualizer.

Can choose gaussian or sin source, and control parameters.

Boundary conditions support absorbing and dirichlet.

Real time fourier transforms of E field at source location, transmit location, and reflect location to analyze spectral response of device.

Device can be constructed easily using the 'eps' and 'mu' objects in the text file.  
Can add arbitrary number of step functions in the form of an array:
eg:  

    'eps' : [
			([100,200], 2),
			([200,300], 3),
			([300,400], 4),
			]

gives positions 100-200 relative eps of 2 and 200-300 relative eps of 3 ... etc.
			
This data is displayed for reference while the main time loop runs.

All paramaters are fed to aux.py through a text file for ease of use.  Structure is as follows:

    {
    	'length'    : [integer: number of grid points],
    	'tMax'      : [integer: number of time steps],
    	'source'    : {
    		'loc'   	: [integer: source entry position],
    		'type'  	: [string: 'g' or 's' (gaussian or sin)],
    		'tfsf'  	: [boolean: True or False (total field scatter field)],
    		'width'     : [integer: source pulse width in time],
    		'height'    : [integer: source amplitude],
    		'offset'    : [integer: source phase or lag time]
    	},
    	'env'       : {
    		'eps' : [
    			([[integer: starting index],[integer: ending index]], [integer: relative epsilon value]),
          ...
          ...
    		],
    		'mu' : [
    			([[integer: starting index],[integer: ending index]], [integer: relative mu value]),
          ...
          ...
    		],
    	},
    	'skip'      : [integer: animation skip rate (100 -> show 1 out of 100 frames)],
    	'freq'      : {
    		'min'   : [integer: min frequency for fourier plots],
    		'max'   : [integer: max frequency for fourier plots],
    		'n'     : [integer: number of frequencies in fourier plots]
    	},
    	'bound'     : [string: 'd' or 'a', dirichlet (conductor) boundary condition or absorbing boundary condition],
    }

If multiple devices / testing environments are prefered.  May create multiple input files in this directory.  Then change line 9 of aux.py


    	with open('yourNewinput.txt','r') as inf:
    		params = eval(inf.read())
    	return params
    	
to the text file you would like to run.

To run the project.  Run

    python fdtd1d.py
    



