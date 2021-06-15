import re

# 用于测试flexGet正则分类

def extract1(pattern, value, des):
    match = re.search(pattern, value, re.I | re.U)
    if match:
        groups = [x for x in match.groups() if x is not None]
        print('groups: {}', groups)
        value = ' '.join(groups).strip()
        print('field  after extract: `{}`', value)
        print(des)
        return value
    return value


def replace(pattern, format, value):
    regexp = re.compile(pattern, flags=re.I | re.U)
    value = regexp.sub(format, value)
    return value


def extract(field_value):
    regexp = re.compile('_', flags=re.I | re.U)
    field_value = regexp.sub(r' ', field_value).strip()

    print(field_value)
    # 正则顺序原则上，尽量将解析带 season 的放前面。防止被解析成无 season的格式
    # 添加新规则请尽量确保原有类型名称也能继续正常解析
    # 最后的输出内容如果是    番名 S0X - E0X - 1080p 或者  番名  - E0X - 1080p  这种格式即表示能够完成分类
    # 如下方示例中的            IJIRANAIDE, NAGATORO SAN - E01 - 1080P

    # [IJIRANAIDE, NAGATORO SAN][01][BIG5][1080P]
    # groups: {} ['IJIRANAIDE, NAGATORO SAN', '01', '1080P']
    # field  after extract: `{}` IJIRANAIDE, NAGATORO SAN 01 1080P
    # 格式7
    # IJIRANAIDE, NAGATORO SAN - E01 - 1080P

    field_value = extract1('(?:\[.+?\]) (.+?) (\d*)(?:nd|rd|th) (?:.+? )-\s(\d+)\s\[(.+?)\]', field_value, "格式1");
    field_value = extract1('(?:\[.+?\]) (.+?) (\d*)(?:nd|rd|th) (?:Season )-\s(\d+)\s(?:END)\s\[(.+?)\].*',
                           field_value, "格式2");
    field_value = extract1('(?:\[.+?\]) (.+?) (?:Season )(\d*)(?:.*?)(\d+)(?:.*?)(\d{3,4}\w).*', field_value, "格式3");
    field_value = extract1('(?:\[.+?\]) (.+?) (?:-\s)?(\d+)(?:.*?)(\d{3,4}\w).*', field_value, "格式4");
                     #[Nekomoe kissaten] [ Hataraku Saibou S2   ][   04        ][       1080p            ][CHS]
                     #(?:\[.+?\[)                 (.+?)    \]\[      (\d*) (?:\].*?\[)  (\d{3,4}\w)   \].*
    field_value = extract1('(?:\[.+?\[)(.+?)\]\[(\d*)(?:\].*?\[)(\d{3,4}\w)\].*', field_value, "格式5");

    field_value = extract1('(?:\[.+?\[)(.+?)\]\[(\d*)(?:\].*?\[)(\d{3,4}\w).*', field_value, "格式6");
    field_value = extract1('(?:\[)(.+?)\]\[(\d*)(?:\].*?\[)(\d{3,4}\w)\].*', field_value, "格式7");

    field_value = replace('(.*) (\d+) (\d+) (.*)', r'\1 - S0\2E\3 - \4', field_value)
    field_value = replace('(.*) (\d+) (\d+\w)', r'\1 - E\2 - \3', field_value)

    print(field_value + "\n")




field = "[Erai-raws] Boku no Hero Academia 3rd Season - 25 [1080p][Multiple Subtitle]"
extract(field)
field = "[Erai-raws] Kyoukai no Rinne (TV) 3rd Season - 01 [1080p][Multiple Subtitle]"
extract(field)

field = "[Erai-raws] Gintama. Shirogane no Tamashii-hen 2nd Season - 14 END [1080p][Multiple Subtitle]"
extract(field)

field = "[Lilith-Raws] Test Regex S2 - 05 [Baha][WEB-DL][1080p][AVC AAC][CHT][MP4]"
extract(field)
field = "[Lilith-Raws] Tenchi Souzou Design Bu - 01 [Baha][WEB-DL][1080p][AVC AAC][CHT][MP4]"
extract(field)
field = "[BeanSub&FZSD&LoliIHouse] Dr. Stone S2 - 01 [WebRip 1080p HEVC-10bit AAC]"
extract(field)
field = "[Lilith-Raws] Test Regex S2 - 05 [Baha][WEB-DL][1080p][AVC AAC][CHT][MP4]"
extract(field)
field = "[Lilith-Raws] Tenchi Souzou Design Bu - 01 [Baha][WEB-DL][1080p][AVC AAC][CHT][MP4]"
extract(field)

field = "[BeanSub][Shingeki_no_Kyojin][64][BIG5][1080P][x264_AAC].mp4"
extract(field)
field = "[KTXP][Yakusoku_no_Neverland_S2][01][GB][1080p]"
extract(field)

field = "[Sakurato] Yuru Camp Season 2 [01][AVC-8bit 1080p AAC][CHS]"
extract(field)

field = "[Nekomoe kissaten] Mushoku Tensei 01 [WebRip 1080p HEVC-10bit AAC ASSx2]"
extract(field)

field = "[VCB-Studio] Log Horizon [06][Ma10p_1080p][x265_flac]"
extract(field)

field = "[VCB-Studio] Log Horizon 2 [06][Ma10p_1080p][x265_flac]"
extract(field)

field = "[Nekomoe kissaten][Hataraku Saibou S2][04][1080p][CHS]"
extract(field)


field = "[Airota][Kobayashi-san Chi no Maid Dragon - Minidora][01][1080p HEVC-10bit AAC ASS]"
extract(field)
field = "[XKsub][Godzilla S.P][01][1080p HEVC-10bit][WEBRip][MKV]"
extract(field)
field = "[IJIRANAIDE, NAGATORO SAN][01][BIG5][1080P]"
extract(field)