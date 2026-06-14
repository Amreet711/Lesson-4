Amount=int(input("How much money do you have?:"))
note_1=Amount//100
remainder_note1=Amount%100
note_2=remainder_note1//50
remainder_note2=remainder_note1%50
note_3=remainder_note2//10
print(Amount,"is made from",note_1,"100 ruppe notes and",note_2,"50 rupee notes and", note_3,"10 rupee notes")