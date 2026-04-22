from flask import Flask, request, render_template
from guardrails.input_filter import filter_input
from guardrails.injection import detect_injection
from guardrails.output_filter import filter_output
from llm.api_client import call_llm
from utils.logger import log_unsafe_input, log_unsafe_output

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        user_input = request.form['user_input']
        
        # Input Guardrail
        safe_input, reason = filter_input(user_input)
        if not safe_input:
            log_unsafe_input(user_input, reason)
            response = f'❌ Unsafe input detected: {reason}'
            return render_template('index.html', response=response)
        
        # Injection Detection
        no_injection, reason = detect_injection(user_input)
        if not no_injection:
            log_unsafe_input(user_input, reason)
            response = f'❌ Potential prompt injection detected: {reason}'
            return render_template('index.html', response=response)
        
        # Call LLM
        llm_response = call_llm(user_input)
        
        # Output Guardrail
        safe_output, reason = filter_output(llm_response)
        if not safe_output:
            log_unsafe_output(llm_response, reason)
            response = '❌ The response was filtered for safety reasons.'
        else:
            response = llm_response
    
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)