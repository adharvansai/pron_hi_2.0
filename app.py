from flask import Flask, render_template, request, url_for, flash, redirect
from highlightHelper.configDict import IPA_DICT,COLORS
from highlightHelper.highlighter import highlight_text
import json



app = Flask(__name__)
app.config['SECRET_KEY'] = 'f8e8a8244e245e9627363ec1d181d6c3e2a02b30773494ac'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/highlighted', methods=['GET', 'POST'])
def highlighter():
    if(request.method == "POST"):
        ipa_ckb = request.form.getlist('ipa_ckb')
        text_input = request.form.get('user_input')
        text_input_split = text_input.split(" ")
        req_ipa = []
        for i in ipa_ckb:
            req_ipa.append(IPA_DICT[int(i)])

        word_ind = highlight_text(text_input_split,req_ipa)
        mark_text = "<mark class='ph1' style='background: COLOR!important'>WORDTEXT</mark>"
        for i,k in enumerate(word_ind.keys()):
            curr_mark = mark_text.replace("COLOR",COLORS[i])
            for ind in word_ind[k]:
                text_input_split[ind] = curr_mark.replace("WORDTEXT", text_input_split[ind])
        final_text = " ".join(text_input_split)

        return render_template('highlighted.html', text = final_text, original_text = text_input )#request.args['user_input'])
