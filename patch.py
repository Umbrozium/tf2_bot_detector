import re
with open('tf2_bot_detector/Config/ConfigHelpers.h', 'r', encoding='utf-8') as f: content = f.read()
content = re.sub(r'(?s)(// END ConfigSchemaInfo.*?)(template<typename T>\s*class ConfigFileGroupBase)', r'\1}\n\n#include <fmt/ostream.h>\n\ntemplate <typename CharT>\nstruct fmt::formatter<tf2_bot_detector::ConfigSchemaInfo, CharT> : fmt::ostream_formatter {};\n\nnamespace tf2_bot_detector\n{\n\t\2', content)
with open('tf2_bot_detector/Config/ConfigHelpers.h', 'w', encoding='utf-8') as f: f.write(content)
