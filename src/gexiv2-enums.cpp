
/* Generated data (by glib-mkenums) */

#include "gexiv2-enums.h"
/* enumerations from "./gexiv2/gexiv2-metadata.h" */
#include "./gexiv2/gexiv2-metadata.h"
GType
gexiv2_gexiv2_orientation_get_type (void)
{
    static GType type = 0;


    if (!type)
    {
        static const GEnumValue _gexiv2_gexiv2_orientation_values[] = {
            { GEXIV2_ORIENTATION_UNSPECIFIED, "GEXIV2_ORIENTATION_UNSPECIFIED", "unspecified" },
            { GEXIV2_ORIENTATION_NORMAL, "GEXIV2_ORIENTATION_NORMAL", "normal" },
            { GEXIV2_ORIENTATION_HFLIP, "GEXIV2_ORIENTATION_HFLIP", "hflip" },
            { GEXIV2_ORIENTATION_ROT_180, "GEXIV2_ORIENTATION_ROT_180", "rot-180" },
            { GEXIV2_ORIENTATION_VFLIP, "GEXIV2_ORIENTATION_VFLIP", "vflip" },
            { GEXIV2_ORIENTATION_ROT_90_HFLIP, "GEXIV2_ORIENTATION_ROT_90_HFLIP", "rot-90-hflip" },
            { GEXIV2_ORIENTATION_ROT_90, "GEXIV2_ORIENTATION_ROT_90", "rot-90" },
            { GEXIV2_ORIENTATION_ROT_90_VFLIP, "GEXIV2_ORIENTATION_ROT_90_VFLIP", "rot-90-vflip" },
            { GEXIV2_ORIENTATION_ROT_270, "GEXIV2_ORIENTATION_ROT_270", "rot-270" },
            { 0, NULL, NULL }
        };

        type = g_enum_register_static ("GExiv2Orientation", _gexiv2_gexiv2_orientation_values);
    }


  return type;
}
GType
gexiv2_gexiv2_structure_type_get_type (void)
{
    static GType type = 0;


    if (!type)
    {
        static const GEnumValue _gexiv2_gexiv2_structure_type_values[] = {
            { GEXIV2_STRUCTURE_XA_NONE, "GEXIV2_STRUCTURE_XA_NONE", "none" },
            { GEXIV2_STRUCTURE_XA_ALT, "GEXIV2_STRUCTURE_XA_ALT", "alt" },
            { GEXIV2_STRUCTURE_XA_BAG, "GEXIV2_STRUCTURE_XA_BAG", "bag" },
            { GEXIV2_STRUCTURE_XA_SEQ, "GEXIV2_STRUCTURE_XA_SEQ", "seq" },
            { GEXIV2_STRUCTURE_XA_LANG, "GEXIV2_STRUCTURE_XA_LANG", "lang" },
            { 0, NULL, NULL }
        };

        type = g_enum_register_static ("GExiv2StructureType", _gexiv2_gexiv2_structure_type_values);
    }


  return type;
}
GType
gexiv2_gexiv2_xmp_format_flags_get_type (void)
{
    static GType type = 0;


    if (!type)
    {
        static const GFlagsValue _gexiv2_gexiv2_xmp_format_flags_values[] = {
            { GEXIV2_OMIT_PACKET_WRAPPER, "GEXIV2_OMIT_PACKET_WRAPPER", "omit-packet-wrapper" },
            { GEXIV2_READ_ONLY_PACKET, "GEXIV2_READ_ONLY_PACKET", "read-only-packet" },
            { GEXIV2_USE_COMPACT_FORMAT, "GEXIV2_USE_COMPACT_FORMAT", "use-compact-format" },
            { GEXIV2_INCLUDE_THUMBNAIL_PAD, "GEXIV2_INCLUDE_THUMBNAIL_PAD", "include-thumbnail-pad" },
            { GEXIV2_EXACT_PACKET_LENGTH, "GEXIV2_EXACT_PACKET_LENGTH", "exact-packet-length" },
            { GEXIV2_WRITE_ALIAS_COMMENTS, "GEXIV2_WRITE_ALIAS_COMMENTS", "write-alias-comments" },
            { GEXIV2_OMIT_ALL_FORMATTING, "GEXIV2_OMIT_ALL_FORMATTING", "omit-all-formatting" },
            { 0, NULL, NULL }
        };

        type = g_flags_register_static ("GExiv2XmpFormatFlags", _gexiv2_gexiv2_xmp_format_flags_values);
    }


  return type;
}
/* enumerations from "./gexiv2/gexiv2-log.h" */
#include "./gexiv2/gexiv2-log.h"
GType
gexiv2_gexiv2_log_level_get_type (void)
{
    static GType type = 0;


    if (!type)
    {
        static const GEnumValue _gexiv2_gexiv2_log_level_values[] = {
            { GEXIV2_LOG_LEVEL_DEBUG, "GEXIV2_LOG_LEVEL_DEBUG", "debug" },
            { GEXIV2_LOG_LEVEL_INFO, "GEXIV2_LOG_LEVEL_INFO", "info" },
            { GEXIV2_LOG_LEVEL_WARN, "GEXIV2_LOG_LEVEL_WARN", "warn" },
            { GEXIV2_LOG_LEVEL_ERROR, "GEXIV2_LOG_LEVEL_ERROR", "error" },
            { GEXIV2_LOG_LEVEL_MUTE, "GEXIV2_LOG_LEVEL_MUTE", "mute" },
            { 0, NULL, NULL }
        };

        type = g_enum_register_static ("GExiv2LogLevel", _gexiv2_gexiv2_log_level_values);
    }


  return type;
}

/* Generated data ends here */

