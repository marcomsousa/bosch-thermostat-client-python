"""Heating Circuits module of Bosch thermostat."""
import logging
from .const import (
    SUBMIT,
    HC,
    AUTO_SETPOINT,
    MANUAL_SETPOINT,
    OPERATION_MODE,
    AUTO_SETTEMP,
)
from .circuit import Circuit


_LOGGER = logging.getLogger(__name__)


class HeatingCircuit(Circuit):
    """Single Heating Circuits object."""

    def __init__(self, requests, attr_id, db, str_obj):
        """
        Initialize heating circuit.

        :param obj get_request:    function to retrieve data from thermostat.
        :param obj submit_request: function to send data to thermostat.
        :param str hc_name: name of heating circuit.
        """
        super().__init__(requests, attr_id, db, str_obj, HC)

    @property
    def temp_setpoint(self):
        """Check whith temp property. Use only for setting temp."""
        operation_mode = self.get_value(OPERATION_MODE)
        if operation_mode:
            return AUTO_SETPOINT if operation_mode == self._str.auto else MANUAL_SETPOINT
        return None

    async def set_temperature(self, temperature):
        """Set temperature of Circuit."""
        temp_property = AUTO_SETTEMP if self.temp_setpoint == AUTO_SETPOINT else self.temp_setpoint    
        if temp_property:
            await self._requests[SUBMIT](self._circuits_path[temp_property], temperature
            )
            self._data[self.temp_setpoint][self._str.val] = temperature
            return True
        return False

    @property
    def target_temperature(self):
        """Get target temperature of Circtuit. Temporary or Room set point."""
        _LOGGER.debug("Target temp is %s", self.get_value(self.temp_setpoint))
        return self.get_value(self.temp_setpoint)
