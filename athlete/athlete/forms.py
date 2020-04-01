from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    id_num = forms.IntegerField()

    #class Meta():
     #   model = Form
      #  fields = ('first_name', 'last_name', 'id_num')

#class SportForm (forms.ModelForm):
 #   OPTIONS  = (
 #       ("WBBALL", "Women's Basketball"),
  #      ("MBBALL", "Men's Basketball"),
   #     ("SBALL", "Softball"),
    #    ("BBALL", "Baseball"),
     #   ("TF", "Track and Field"),
      #  ("XC", "Cross Country"),
       # ("FBAll", "Football"),
        #("CHEER", "Cheerleading")
    #)
    #Sports = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
     #                                          choices=OPTIONS)