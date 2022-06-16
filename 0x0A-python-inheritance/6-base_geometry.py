#!/usr/bin/python3
'''A module for working with geometry.
'''


class BaseGeometry:
    '''The base class for all geometry objects.
    '''
    def area(self):
        '''Computes the area of this geometry.

        Returns:
            float: The area of this geometry object.
        '''
        raise Exception('area() is not implemented')
