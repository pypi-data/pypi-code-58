import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c, sensor
from esphome.const import CONF_HUMIDITY, CONF_ID, CONF_TEMPERATURE, \
    ICON_THERMOMETER, UNIT_CELSIUS, UNIT_PERCENT, ICON_WATER_PERCENT

DEPENDENCIES = ['i2c']

htu21d_ns = cg.esphome_ns.namespace('htu21d')
HTU21DComponent = htu21d_ns.class_('HTU21DComponent', cg.PollingComponent, i2c.I2CDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(HTU21DComponent),
    cv.Required(CONF_TEMPERATURE): sensor.sensor_schema(UNIT_CELSIUS, ICON_THERMOMETER, 1),
    cv.Required(CONF_HUMIDITY): sensor.sensor_schema(UNIT_PERCENT, ICON_WATER_PERCENT, 1),
}).extend(cv.polling_component_schema('60s')).extend(i2c.i2c_device_schema(0x40))


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield i2c.register_i2c_device(var, config)

    if CONF_TEMPERATURE in config:
        sens = yield sensor.new_sensor(config[CONF_TEMPERATURE])
        cg.add(var.set_temperature(sens))

    if CONF_HUMIDITY in config:
        sens = yield sensor.new_sensor(config[CONF_HUMIDITY])
        cg.add(var.set_humidity(sens))
