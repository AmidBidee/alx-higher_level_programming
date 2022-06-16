#!/usr/bin/python3
'''A module containing a rebellious int.
'''


class MyInt(int):
    '''Represents a rebellious integer object.
    '''
    def __eq__(self, value):
        '''Checks if the given value is not equal to the
        value of this object.

        Args:
            value (MyInt): The value to be compared against.

        Returns:
            bool: True if the value is not equal to the value
            stored by this object.
        '''
        return super().__ne__(value)

    def __ne__(self, value):
        '''Checks if the given value is equal to the value
        of this object.

        Args:
            value (MyInt): The value to be compared against.

        Returns:
            bool: True if the value is equal to the value
            stored by this object.
        '''
        return super().__eq__(value)
