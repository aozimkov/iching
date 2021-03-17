#-*- coding:utf-8 -*-

# asset list of hexagrams
hexagon_numbers_dict = {
'111111': 1,
'000000': 2,
'100010': 3,
'010001': 4,
'111010': 5,
'010111': 6,
'010000': 7,
'000010': 8,
'111011': 9,
'110111': 10,
'111000': 11,
'000111': 12,
'101111': 13,
'111101': 14,
'001000': 15,
'000100': 16,
'100110': 17,
'011001': 18,
'110000': 19,
'000011': 20,
'100101': 21,
'101001': 22,
'000001': 23,
'100000': 24,
'100111': 25,
'111001': 26,
'100001': 27,
'011110': 28,
'010010': 29,
'101101': 30,
'001110': 31,
'011100': 32,
'001111': 33,
'111100': 34,
'000101': 35,
'101000': 36,
'101011': 37,
'110101': 38,
'001010': 39,
'010100': 40,
'110001': 41,
'100011': 42,
'111110': 43,
'011111': 44,
'000110': 45,
'011000': 46,
'010110': 47,
'011010': 48,
'101110': 49,
'011101': 50,
'100100': 51,
'001001': 52,
'001011': 53,
'110100': 54,
'101100': 55,
'001101': 56,
'011011': 57,
'110110': 58,
'010011': 59,
'110010': 60,
'110011': 61,
'001100': 62,
'101010': 63,
'010101': 64}

hexagrams = ['Hexagram 1 is named 乾 (qián), "Force". Other variations include "the creative", "strong action", "the key", and "god". Its inner (lower) trigram is ☰ (乾 qián) force = (天) heaven, and its outer (upper) trigram is the same.',
'Hexagram 2 is named 坤 (kūn), "Field". Other variations include "the receptive", "acquiescence", and "the flow". Its inner (lower) trigram is ☷ (坤 kūn) field = (地) earth, and its outer (upper) trigram is identical.',
'Hexagram 3 is named 屯 (zhūn), "Sprouting". Other variations include "difficulty at the beginning", "gathering support", and "hoarding". Its inner (lower) trigram is ☳ (震 zhèn) shake = (雷) thunder, and its outer (upper) trigram is ☵ (坎 kǎn) gorge = (水) water.',
'Hexagram 4 is named 蒙 (méng), "Enveloping". Other variations include "youthful folly", "the young shoot", and "discovering". Its inner trigram is ☵ (坎 kǎn) gorge = (水) water. Its outer trigram is ☶ (艮 gèn) bound = (山) mountain.',
'Hexagram 5 is named 需 (xū), "Attending". Other variations include "waiting", "moistened", and "arriving". Its inner (lower) trigram is ☰ (乾 qián) force = (天) heaven, and its outer (upper) trigram is ☵ (坎 kǎn) gorge = (水) water.',
'Hexagram 6 is named 訟 (sòng), "Arguing". Other variations include "conflict" and "lawsuit". Its inner (lower) trigram is ☵ (坎 kǎn) gorge = (水) water, and its outer (upper) trigram is ☰ (乾 qián) force = (天) heaven.',
'Hexagram 7 is named 師 (shī), "Leading". Other variations include "the army" and "the troops". Its inner (lower) trigram is ☵ (坎 kǎn) gorge = (水) water, and its outer (upper) trigram is ☷ (坤 kūn) field = (地) earth.',
'Hexagram 8 is named 比 (bǐ), "Grouping". Other variations include "holding together" and "alliance". Its inner (lower) trigram is ☷ (坤 kūn) field = (地) earth, and its outer (upper) trigram is ☵ (坎 kǎn) gorge = (水) water.',
'Hexagram 9 is named 小畜 (xiǎo chù), "Small Accumulating". Other variations include "the taming power of the small" and "small harvest". Its inner (lower) trigram is ☰ (乾 qián) force = (天) heaven, and its outer (upper) trigram is ☴ (巽 xùn) ground = (風) wind.',
'Hexagram 10 is named 履 (lǚ), "Treading". Other variations include "treading (conduct)" and "continuing". Its inner (lower) trigram is ☱ (兌 duì) open = (澤) swamp, and its outer (upper) trigram is ☰ (乾 qián) force = (天) heaven.',
'Hexagram 11 is named 泰 (tài), "Pervading". Other variations include "peace" and "greatness". Its inner (lower) trigram is ☰ (乾 qián) force = (天) heaven, and its outer (upper) trigram is ☷ (坤 kūn) field = (地) earth.',
'Hexagram 12 is named 否 (pǐ), "Obstruction". Other variations include "standstill (stagnation)" and "selfish persons". Its inner (lower) trigram is ☷ (坤 kūn) field = (地) earth, and its outer (upper) trigram is ☰ (乾 qián) force = (天) heaven.',
'Hexagram 13 is named 同人 (tóng rén), "Concording People". Other variations include "fellowship with men" and "gathering men". Its inner (lower) trigram is ☲ (離 lí) radiance = (火) fire, and its outer (upper) trigram is ☰ (乾 qián) force = (天) heaven.',
'Hexagram 14 is named 大有 (dà yǒu), "Great Possessing". Other variations include "possession in great measure" and "the great possession". Its inner (lower) trigram is ☰ (乾 qián) force = (天) heaven, and its outer (upper) trigram is ☲ (離 lí) radiance = (火) fire.',
'Hexagram 15 is named 謙 (qiān), "Humbling". Other variations include "modesty". Its inner (lower) trigram is ☶ (艮 gèn) bound = (山) mountain and its outer (upper) trigram is ☷ (坤 kūn) field = (地) earth.',
'Hexagram 16 is named 豫 (yù), "Providing-For". Other variations include "enthusiasm" and "excess". Its inner (lower) trigram is ☷ (坤 kūn) field = (地) earth, and its outer (upper) trigram is ☳ (震 zhèn) shake = (雷) thunder.',
'Hexagram 17 is named 隨 (suí), "Following". Its inner (lower) trigram is ☳ (震 zhèn) shake = (雷) thunder, and its outer (upper) trigram is ☱ (兌 duì) open = (澤) swamp.',
'Hexagram 18 is named 蠱 (gǔ), "Correcting". Other variations include "work on what has been spoiled (decay)", decaying and "branch".[1] Its inner (lower) trigram is ☴ (巽 xùn) ground = (風) wind, and its outer (upper) trigram is ☶ (艮 gèn) bound = (山) mountain. Gu is the name of a venom-based poison traditionally used in Chinese witchcraft.',
'Hexagram 19 is named 臨 (lín), "Nearing". Other variations include "approach" and "the forest". Its inner (lower) trigram is ☱ (兌 duì) open = (澤) swamp, and its outer (upper) trigram is ☷ (坤 kūn) field = (地) earth.',
'Hexagram 20 is named 觀 (guān), "Viewing". Other variations include "contemplation (view)" and "looking up". Its inner (lower) trigram is ☷ (坤 kūn) field = (地) earth, and its outer (upper) trigram is ☴ (巽 xùn) ground = (風) wind.',
'Hexagram 21 is named 噬嗑 (shì kè), "Gnawing Bite". Other variations include "biting through" and "biting and chewing". Its inner (lower) trigram is ☳ (震 zhèn) shake = (雷) thunder, and its outer trigram is ☲ (離 lí) radiance = (火) fire. [2]',
'Hexagram 22 is named 賁 (bì), "Adorning". Other variations include "grace" and "luxuriance". Its inner (lower) trigram is ☲ (離 lí) radiance = (火) fire, and its outer (upper) trigram is ☶ (艮 gèn) bound = (山) mountain. [3]',
'Hexagram 23 is named 剝 (bō), "Stripping". Other variations include "splitting apart" and "flaying". Its inner trigram is ☷ (坤 kūn) field = (地) earth, and its outer trigram is ☶ (艮 gèn) bound = (山) mountain.',
'Hexagram 24 is named 復 (fù), "Returning". Other variations include "return (the turning point)". Its inner trigram is ☳ (震 zhèn) shake = (雷) thunder, and its outer trigram is ☷ (坤 kūn) field = (地) earth.',
'Hexagram 25 is named 無妄 (wú wàng), "Without Embroiling". Other variations include "innocence (the unexpected)" and "pestilence". Its inner trigram is ☳ (震 zhèn) shake = (雷) thunder, and its outer trigram is ☰ (乾 qián) force = (天) heaven.',
'Hexagram 26 is named 大畜 (dà chù), "Great Accumulating". Other variations include "the taming power of the great", "great storage", and "potential energy". Its inner trigram is ☰ (乾 qián) force = (天) heaven, and its outer trigram is ☶ (艮 gèn) bound = (山) mountain.',
'Hexagram 27 is named 頤 (yí), "Swallowing". Other variations include "the corners of the mouth (providing nourishment)", "jaws" and "comfort/security". Its inner trigram is ☳ (震 zhèn) shake = (雷) thunder, and its outer trigram is ☶ (艮 gèn) bound = (山) mountain.',
'Hexagram 28 is named 大過 (dà guò), "Great Exceeding". Other variations include "preponderance of the great", "great surpassing" and "critical mass". Its inner trigram is ☴ (巽 xùn) ground = (風) wind, and its outer trigram is ☱ (兌 duì) open = (澤) swamp.',
'Hexagram 29 is named 坎 (kǎn), "Gorge". Other variations include "the abyss" (in the oceanographic sense) and "repeated entrapment". Its inner trigram is ☵ (坎 kǎn) gorge = (水) water, and its outer trigram is identical.',
'Hexagram 30 is named 離 (lí), "Radiance". Other variations include "the clinging, fire" and "the net". Its inner trigram is ☲ (離 lí) radiance = (火) fire, and its outer trigram is identical. The origin of the character has its roots in symbols of long-tailed birds such as the peacock or the legendary phoenix.',
'Hexagram 31 is named 咸 (xián), "Conjoining". Other variations include "influence (wooing)" and "feelings". Its inner trigram is ☶ (艮 gèn) bound = (山) mountain, and its outer trigram is ☱ (兌 duì) open = (澤) swamp.',
'Hexagram 32 is named 恆 (héng), "Persevering". Other variations include "duration" and "constancy". Its inner trigram is ☴ (巽 xùn) ground = (風) wind, and its outer trigram is ☳ (震 zhèn) shake = (雷) thunder.',
'Hexagram 33 is named 遯 (dùn), "Retiring". Other variations include "retreat" and "yielding". Its inner trigram is ☶ (艮 gèn) bound = (山) mountain, and its outer trigram is ☰ (乾 qián) force = (天) heaven.',
'Hexagram 34 is named 大壯 (dà zhuàng), "Great Invigorating". Other variations include "the power of the great" and "great maturity". Its inner trigram is ☰ (乾 qián) force = (天) heaven, and its outer trigram is ☳ (震 zhèn) shake = (雷) thunder.',
'Hexagram 35 is named 晉 (jìn), "Prospering". Other variations include "progress" and "aquas". Its inner trigram is ☷ (坤 kūn) field = (地) earth, and its outer trigram is ☲ (離 lí) radiance = (火) fire.',
'Hexagram 36 is named 明夷 (míng yí), "Darkening of the Light". Other variations include "brilliance injured" and "intelligence hidden". Its inner trigram is ☲ (離 lí) radiance = (火) fire, and its outer trigram is ☷ (坤 kūn) field = (地) earth.',
'Hexagram 37 is named 家人 (jiā rén), "Dwelling People". Other variations include "the family (the clan)" and "family members". Its inner trigram is ☲ (離 lí) radiance = (火) fire, and its outer trigram is ☴ (巽 xùn) ground = (風) wind.',
'Hexagram 38 is named 睽 (kuí), "Polarising". Other variations include "opposition" and "perversion". Its inner trigram is ☱ (兌 duì) open = (澤) swamp, and its outer trigram is ☲ (離 lí) radiance = (火) fire.',
'Hexagram 39 is named 蹇 (jiǎn), "Limping". Other variations include "obstruction" and "afoot". Its inner trigram is ☶ (艮 gèn) bound = (山) mountain, and its outer trigram is ☵ (坎 kǎn) gorge = (水) water.',
'Hexagram 40 is named 解 (xiè), "Taking-Apart". Other variations include "deliverance" and "untangled". Its inner trigram is ☵ (坎 kǎn) gorge = (水) water, and its outer trigram is ☳ (震 zhèn) shake = (雷) thunder.',
'Hexagram 41 is named 損 (sǔn), "Diminishing". Other variations include "decrease". Its inner trigram is ☱ (兌 duì) open = (澤) swamp, and its outer trigram is ☶ (艮 gèn) bound = (山) mountain.',
'Hexagram 42 is named 益 (yì), "Augmenting". Other variations include "increase". Its inner trigram is ☳ (震 zhèn) shake = (雷) thunder, and its outer trigram is ☴ (巽 xùn) ground = (風) wind.',
'Hexagram 43 is named 夬 (guài), "Displacement". Other variations include "resoluteness", "parting", and "break-through". Its inner trigram is ☰ (乾 qián) force = (天) heaven, and its outer trigram is ☱ (兌 duì) open = (澤) swamp.',
'Hexagram 44 is named 姤 (gòu), "Coupling". Other variations include "coming to meet" and "meeting". Its inner trigram is ☴ (巽 xùn) ground = (風) wind, and its outer trigram is ☰ (乾 qián) force = (天) heaven.',
'Hexagram 45 is named 萃 (cuì), "Clustering". Other variations include "gathering together (massing)" and "finished". Its inner trigram is ☷ (坤 kūn) field = (地) earth, and its outer trigram is ☱ (兌 duì) open = (澤) swamp.',
'Hexagram 46 is named 升 (shēng), "Ascending". Other variations include "pushing upward". Its inner trigram is ☴ (巽 xùn) ground = (風) wind, and its outer trigram is ☷ (坤 kūn) field = (地) earth.',
'Hexagram 47 is named 困 (kùn), "Confining". Other variations include "oppression (exhaustion)" and "entangled". Its inner trigram is ☵ (坎 kǎn) gorge = (水) water, and its outer trigram is ☱ (兌 duì) open = (澤) swamp.',
'Hexagram 48 is named 井 (jǐng), "Welling". Other variations include "the well". Its inner trigram is ☴ (巽 xùn) ground = (風) wind, and its outer trigram is ☵ (坎 kǎn) gorge = (水) water.',
'Hexagram 49 is named 革 (gé), "Skinning". Other variations include "revolution (molting)" and "the bridle". Its inner trigram is ☲ (離 lí) radiance = (火) fire, and its outer trigram is ☱ (兌 duì) open = (澤) swamp.',
'Hexagram 50 is named 鼎 (dǐng), "Holding". Other variations include "the cauldron". Its inner trigram is ☴ (巽 xùn) ground = (風) wind, and its outer trigram is ☲ (離 lí) radiance = (火) fire.',
'Hexagram 51 is named 震 (zhèn), "Shake". Other variations include "the arousing (shock, thunder)" and "thunder". Both its inner and outer trigrams are ☳ (震 zhèn) shake = (雷) thunder.',
'Hexagram 52 is named 艮 (gèn), "Bound". Other variations include "keeping still, mountain" and "stilling". Both its inner and outer trigrams are ☶ (艮 gèn) bound = (山) mountain.',
'Hexagram 53 is named 漸 (jiàn), "Infiltrating". Other variations include "development (gradual progress)" and "advancement". Its inner trigram is ☶ (艮 gèn) bound = (山) mountain, and its outer trigram is ☴ (巽 xùn) ground = (風) wind.',
'Hexagram 54 is named 歸妹 (guī mèi), "Converting the Maiden". Other variations include "the marrying maiden" and "returning maiden". Its inner trigram is ☱ (兌 duì) open = (澤) swamp, and its outer trigram is ☳ (震 zhèn) shake = (雷) thunder.',
'Hexagram 55 is named 豐 (fēng), "Abounding". Other variations include "abundance" and "fullness". Its inner trigram is ☲ (離 lí) radiance = (火) fire, and its outer trigram is ☳ (震 zhèn) shake = (雷) thunder.',
'Hexagram 56 is named 旅 (lǚ), "Sojourning". Other variations include "the wanderer" and "traveling". Its inner trigram is ☶ (艮 gèn) bound = (山) mountain, and its outer trigram is ☲ (離 lí) radiance = (火) fire.',
'Hexagram 57 is named 巽 (xùn), "Ground". Other variations include "the gentle (the penetrating, wind)" and "calculations". Both its inner and outer trigrams are ☴ (巽 xùn) ground = (風) wind.',
'Hexagram 58 is named 兌 (duì), "Open". Other variations include "the joyous, lake" and "usurpation". Both its inner and outer trigrams are ☱ (兌 duì) open = (澤) swamp.',
'Hexagram 59 is named 渙 (huàn), "Dispersing". Other variations include "dispersion (dissolution)" and "dispersal". Its inner trigram is ☵ (坎 kǎn) gorge = (水) water, and its outer trigram is ☴ (巽 xùn) ground = (風) wind.',
'Hexagram 60 is named 節 (jié), "Articulating". Other variations include "limitation" and "moderation". Its inner trigram is ☱ (兌 duì) open = (澤) swamp, and its outer trigram is ☵ (坎 kǎn) gorge = (水) water.',
'Hexagram 61 is named 中孚 (zhōng fú), "Center Returning". Other variations include "inner truth" and "central return". Its inner trigram is ☱ (兌 duì) open = (澤) swamp, and its outer trigram is ☴ (巽 xùn) ground = (風) wind.',
'Hexagram 62 is named 小過 (xiǎo guò), "Small Exceeding". Other variations include "preponderance of the small" and "small surpassing". Its inner trigram is ☶ (艮 gèn) bound = (山) mountain, and its outer trigram is ☳ (震 zhèn) shake = (雷) thunder.',
'Hexagram 63 is named 既濟 (jì jì), "Already Fording". Other variations include "after completion" and "already completed" or "already done" . Its inner trigram is ☲ (離 lí) radiance = (火) fire, and its outer trigram is ☵ (坎 kǎn) gorge = (水) water.',
'Hexagram 64 is named 未濟 (wèi jì), "Not Yet Fording". Other variations include "before completion" and "not yet completed". Its inner trigram is ☵ (坎 kǎn) gorge = (水) water, and its outer trigram is ☲ (離 lí) radiance = (火) fire.']