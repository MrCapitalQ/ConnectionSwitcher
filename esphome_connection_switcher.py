import zigpy.types as t
from zigpy.quirks.v2 import QuirkBuilder, EntityType
from zigpy.zcl.clusters.general import AnalogOutput


class SelectedConnection(t.enum8):
    NoConnection = 0x00
    Connection1 = 0x01
    Connection2 = 0x02
    Connection3 = 0x03


(
    QuirkBuilder("esphome", "connection-switcher")
    .enum(
        AnalogOutput.AttributeDefs.present_value.name,
        SelectedConnection,
        AnalogOutput.cluster_id,
        translation_key="selected_connection",
        fallback_name="Selected Connection",
        entity_type=EntityType.STANDARD,
    )
    .add_to_registry()
)
