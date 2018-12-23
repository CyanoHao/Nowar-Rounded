import sys
import json


def NameFont(font, region, weight, version):

	isStdStyle = weight == 'Regular' or weight == 'Bold'

	font['OS_2']['achVendID'] = 'Cyan'
	font['name'] = [
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 0,
			"nameString": "Copyright © 2018—2019 Cyano Hao, with reserved font name “Nowar”, “有爱”, and “有愛”. Portions Copyright 2015 Google Inc. Portions © 2014, 2015, 2018 Adobe (http://www.adobe.com/)."
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 1,
			"nameString": "Nowar Compact Rounded UI {}".format(region) if isStdStyle else "Nowar Compact Rounded UI {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 2052,
			"nameID": 1,
			"nameString": "有爱窄圆体 UI {}".format(region) if isStdStyle else "有爱窄圆体 UI {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1028,
			"nameID": 1,
			"nameString": "有愛窄圓體 UI {}".format(region) if isStdStyle else "有愛窄圓體 UI {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 3076,
			"nameID": 1,
			"nameString": "有愛窄圓體 UI {}".format(region) if isStdStyle else "有愛窄圓體 UI {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 2,
			"nameString": weight if isStdStyle else "Regular"
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 3,
			"nameString": "Nowar Compact Rounded UI {} {}".format(region, weight) + ' ' + str(version)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 4,
			"nameString": "Nowar Compact Rounded UI {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 2052,
			"nameID": 4,
			"nameString": "有爱窄圆体 UI {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1028,
			"nameID": 4,
			"nameString": "有愛窄圓體 UI {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 3076,
			"nameID": 4,
			"nameString": "有愛窄圓體 UI {} {}".format(region, weight)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 5,
			"nameString": str(version)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 6,
			"nameString": "Nowar-Compact-Rounded-UI-{}-{}".format(region, weight.replace(' ', '-'))
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 8,
			"nameString": "Cyano Hao"
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 9,
			"nameString": "Cyano Hao (round all glyphs); Monotype Design Team (Latin, Greek & Cyrillic); Ryoko NISHIZUKA 西塚涼子 (kana, bopomofo & ideographs); Sandoll Communications 산돌커뮤니케이션, Soo-young JANG 장수영 & Joo-yeon KANG 강주연 (hangul elements, letters & syllables); Dr. Ken Lunde (project architect, glyph set definition & overall production); Masataka HATTORI 服部正貴 (production & ideograph elements)"
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 11,
			"nameString": "https://github.com/CyanoHao"
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 13,
			"nameString": "This Font Software is licensed under the SIL Open Font License, Version 1.1. This Font Software is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the SIL Open Font License for the specific language, permissions and limitations governing your use of this Font Software."
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 14,
			"nameString": "http://scripts.sil.org/OFL"
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 16,
			"nameString": "Nowar Compact Rounded UI {}".format(region)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 2052,
			"nameID": 16,
			"nameString": "有爱窄圆体 UI {}".format(region)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1028,
			"nameID": 16,
			"nameString": "有愛窄圓體 UI {}".format(region)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 3076,
			"nameID": 16,
			"nameString": "有愛窄圓體 UI {}".format(region)
		},
		{
			"platformID": 3,
			"encodingID": 1,
			"languageID": 1033,
			"nameID": 17,
			"nameString": weight
		},
	]

if __name__ == '__main__':
	region = sys.argv[1]
	weight = sys.argv[2]
	encoding = sys.argv[3]
	version = sys.argv[4]

	with open("notor/NotoRounded-Condensed{}.otd".format(weight), 'rb') as baseFile:
		baseFont = json.loads(baseFile.read().decode('UTF-8', errors='replace'))

	with open("rhr/ResourceHanRounded{}-{}.otd".format(region, weight), 'rb') as asianFile:
		asianFont = json.loads(asianFile.read().decode('UTF-8', errors = 'replace'))

	baseFont['OS_2']['ulCodePageRange1'][encoding] = True
	NameFont(baseFont, 'Classic' if region == 'CL' else region, weight, version)

	for (uniId, glyphName) in asianFont['cmap'].items():
		if uniId not in baseFont['cmap'].keys():
			baseFont['cmap'][uniId] = glyphName
			if glyphName not in baseFont['glyf'].keys():
				baseFont['glyf'][glyphName] = asianFont['glyf'][glyphName]

	outStr = json.dumps(baseFont, ensure_ascii=False)
	with open("nowar/{}-NowarCompactRoundedUI-{}-{}.otd".format(encoding, region, weight), 'w') as outFile:
		outFile.write(outStr)
