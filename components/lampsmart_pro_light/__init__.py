import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

# Задаем пространство имен проекта, как в других файлах люстры
lampsmartpro_ns = cg.esphome_ns.namespace('lampsmartpro')

# Указываем ESPHome автоматически загружать и свет, и вентилятор из этой папки
AUTO_LOAD = ["light", "fan"]
DEPENDENCIES = ["esp32"]

CONFIG_SCHEMA = cv.Schema({})
