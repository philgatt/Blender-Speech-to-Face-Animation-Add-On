import bpy

def insert_keyframe(pose, keyframe):
    bpy.ops.object.mode_set(mode='POSE')
    for bone in armature.pose.bones:
        bone.bone.select = True
    bpy.context.scene.frame_set(pose)
    bpy.ops.pose.copy()
    bpy.context.scene.frame_set(keyframe)
    bpy.ops.pose.paste(flipped=False)
    bpy.ops.anim.keyframe_insert(type='LocRotScale')


def animateMesh(props, timeLine):
    PP = props.PP
    FF = props.FF
    TH = props.TH
    DD = props.DD
    kk = props.kk
    CH = props.CH
    SS = props.SS
    nn = props.nn
    RR = props.RR
    aa = props.aa
    E = props.E
    I = props.I
    O = props.O
    U = props.U
    Silent = props.Silent

    print("This animations has ", len(timeLine.timeLine), " frames")
    undefinedChars = []
    for keyframe in range(len(timeLine.timeLine)):

        if timeLine.timeLine[keyframe] != '.':

#            for viseme in visemeNodes:
#                #pm.setKeyframe(visemeNodes[visme], at='weight[0]', v=0, t=keyframe)
#                insert_keyframe(viseme, keyframe)

            case = timeLine.timeLine[keyframe]
            # ["Silent", "PP", "FF", "TH", "DD", "kk", "CH", "SS", "nn", "RR", "aa", "E", "I", "O", "U"]

            if (case == 'ɓ') or (case == 'ɱ') or (case == 'ɯ') or (case == 'ɰ') or (case == 'ʘ') or (case == 'p') or (
                    case == 'b') or (case == 'm'):
                # Viseme:    PP                       Phonemes:      p, b, m                         Word example:           put, bat, mat
                print("1")
                #pm.setKeyframe(visemeNodes["PP"], at='weight[0]', v=1, t=keyframe)
                insert_keyframe(PP, keyframe)
            elif (case == 'β') or (case == 'φ') or (case == 'ɸ') or (case == 'ʋ') or (case == 'ʍ') or (case == 'ŵ') or (case == 'ɰ') or (case == 'ŵ') or (case == 'ẃ') or (case == 'f') or (case == 'v'):
                # Viseme:    FF                       Phonemes:      f, v                            Word example:           fat, vat
                print("2")
                #pm.setKeyframe(visemeNodes["FF"], at='weight[0]', v=1, t=keyframe)
                insert_keyframe(FF, keyframe)
            elif (case == 'ð') or (case == 'θ') or (case == 'þ') or (case == 'ʷ'):
                # Viseme:    TH                       Phonemes:      th                              Word example:           think, that
                print("3")
                #pm.setKeyframe(visemeNodes["TH"], at='weight[0]', v=1, t=keyframe)
                insert_keyframe(TH, keyframe)
            elif (case == 'ɖ') or (case == 'ḍ') or (case == 'ɗ') or (case == 'ʄ') or (case == 'ʈ') or (case == 'ṭ') or (
                    case == 'd') or (case == 't') or (case == '') or (case == ''):
                # Viseme:    DD                       Phonemes:      t, d                            Word example:           tip, doll
                print("4")
                #pm.setKeyframe(visemeNodes["DD"], at='weight[0]', v=1, t=keyframe)
                insert_keyframe(DD, keyframe)
            elif (case == 'ɟ') or (case == 'γ') or (case == 'ɣ') or (case == 'ɠ') or (case == 'ǰ') or (case == 'ʝ') or (
                    case == 'ʲ') or (case == 'ʲ') or (case == 'ɟ') or (case == 'ɥ') or (case == 'ŷ') or (
                    case == 'y') or (case == 'ɰ') or (case == 'ỹ') or (case == 'ȳ') or (case == 'k') or (
                    case == 'g') or (case == 'j') or (case == 'q') or (case == 'x'):
                # Viseme:    kk                       Phonemes:      k, g                            Word example:           call, gas
                print("5")
                #pm.setKeyframe(visemeNodes["kk"], at='weight[0]', v=1, t=keyframe)
                insert_keyframe(kk, keyframe)
            elif (case == 'ç') or (case == 'č') or (case == 'ʃ') or (case == 'ʂ') or (case == 'χ') or (case == 'c'):
                # Viseme:    CH                       Phonemes:      tS, dZ, S                       Word example:           chair, join, she
                print("6")
                #pm.setKeyframe(visemeNodes["CH"], at='weight[0]', v=1, t=keyframe)
                insert_keyframe(CH, keyframe)
            elif (case == 'ɕ') or (case == 'š') or (case == 'ś') or (case == 'ṣ') or (case == 'ẓ') or (case == 'ʒ') or (
                    case == 'ž') or (case == 'ʑ') or (case == 'ʐ') or (case == 's') or (case == 'z'):
                # Viseme:    SS                       Phonemes:      s, z                            Word example:           sir, zeal
                print("7")
                #pm.setKeyframe(visemeNodes["SS"], at='weight[0]', v=1, t=keyframe)
                insert_keyframe(SS, keyframe)
            elif (case == 'ɫ') or (case == 'l') or (case == 'λ') or (case == 'ɭ') or (case == 'ʎ') or (case == 'ɭ') or (
                    case == 'ḷ') or (case == 'ɬ') or (case == 'ɮ') or (case == 'ñ') or (case == 'ŋ') or (
                    case == 'ɲ') or (case == 'ɳ') or (case == 'ṇ') or (case == 'n') or (case == 'l'):
                # Viseme:    nn                       Phonemes:      n, l                            Word example:           lot, not
                print("8")
                #pm.setKeyframe(visemeNodes["nn"], at='weight[0]', v=1, t=keyframe)
                insert_keyframe(nn, keyframe)
            elif (case == 'ɹ') or (case == 'r') or (case == 'ʁ') or (case == 'ř') or (case == 'ɾ') or (case == 'ɽ') or (
                    case == 'ṛ') or (case == 'ɻ'):
                # Viseme:    RR                       Phonemes:      r                               Word example:           red
                print("9")
                #pm.setKeyframe(visemeNodes["RR"], at='weight[0]', v=1, t=keyframe)
                insert_keyframe(RR, keyframe)
            elif (case == 'æ') or (case == 'ɑ') or (case == 'ɐ') or (case == 'ɒ') or (case == 'α') or (case == 'ã') or (
                    case == 'ă') or (case == 'ʌ') or (case == 'a'):
                # Viseme:    aa                       Phonemes:      A:                              Word example:           car
                print("10")
                #pm.setKeyframe(visemeNodes["aa"], at='weight[0]', v=1, t=keyframe)
                insert_keyframe(aa, keyframe)
            elif (case == 'ə') or (case == 'ε') or (case == 'ɛ') or (case == 'ẹ') or (case == 'ɜ') or (case == 'ɚ') or (
                    case == 'ɘ') or (case == 'ẽ') or (case == 'ĕ') or (case == 'e'):
                # Viseme:    E                       Phonemes:      e                                Word example:           bed
                print("11")
                #pm.setKeyframe(visemeNodes["E"], at='weight[0]', v=1, t=keyframe)
                insert_keyframe(E, keyframe)
            elif (case == 'ɪ') or (case == 'i') or (case == 'ɨ') or (case == 'ĩ') or (case == 'ĭ') or (case == '') or (
                    case == '') or (case == '') or (case == '') or (case == 'i'):
                # Viseme:    I                       Phonemes:      ih                               Word example:           tip
                print("12")
                #pm.setKeyframe(visemeNodes["I"], at='weight[0]', v=1, t=keyframe)
                insert_keyframe(I, keyframe)
            elif (case == 'ħ') or (case == 'ɦ') or (case == 'h') or (case == 'ʰ') or (case == 'ɥ') or (case == 'ḥ') or (
                    case == 'ɧ') or (case == 'ø') or (case == 'œ') or (case == 'œ') or (case == 'œ') or (
                    case == 'ö') or (case == 'ɔ') or (case == 'ọ') or (case == 'ɵ') or (case == 'õ') or (
                    case == 'ŏ') or (case == 'o'):
                # Viseme:    O                       Phonemes:      oh                               Word example:           toe
                print("13")
                #pm.setKeyframe(visemeNodes["O"], at='weight[0]', v=1, t=keyframe)
                insert_keyframe(O, keyframe)
            elif (case == 'ʊ') or (case == 'ü') or (case == 'u') or (case == 'ʉ') or (case == 'ɞ') or (case == 'ũ') or (
                    case == 'ŭ') or (case == 'u') or (case == 'ɯ') or (case == 'w') :
                # Viseme:    U                       Phonemes:      ou                               Word example:           book
                print("14")
                #pm.setKeyframe(visemeNodes["U"], at='weight[0]', v=1, t=keyframe)
                insert_keyframe(U, keyframe)
            else:
                print("character is undefined")
                undefinedChars.append(case)

    print("undefined Chars: ")

    for c in undefinedChars:
        print(c)

    for sil in timeLine.silenceTimeLine:
        silStart = round(sil[0] * keyframesPerSecond)
        silEnd = round(sil[1] * keyframesPerSecond)

#        for viseme in visemeNodes:
#            #pm.setKeyframe(visemeNodes[visme], at='weight[0]', v=0, t=silStart)
#            insert_keyframe(viseme, silStart)
#        for visme in visemeNodes:
#            #pm.setKeyframe(visemeNodes[visme], at='weight[0]', v=0, t=silEnd)
#            insert_keyframe(viseme, silEnd)
        #pm.setKeyframe(rest, at='weight[0]', v=1, t=silStart)
        insert_keyframe(Silent, silStart)
        #pm.setKeyframe(rest, at='weight[0]', v=1, t=silEnd)
        insert_keyframe(Silent, silEnd)

#keyframesPerSecondQLineEdit = QtWidgets.QLineEdit("24", parent=wid)
#keyframesPerSecondQLineEdit.move(412, 256)
#silenceTimeCriteriaQLineEdit = QtWidgets.QLineEdit(str(round(5 / 24, 6)), parent=wid)
#silenceTimeCriteriaQLineEdit.move(412, 280)
#silenceCutDownQLineEdit = QtWidgets.QLineEdit(str(round(3 / 24, 6)), parent=wid)
#silenceCutDownQLineEdit.move(412, 304)