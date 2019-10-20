import marvin

'''
Run Flask App for Marvin GUI
'''
marvin.app.run(
    port=9090, # assign to port 5000
    debug=True # Have debug pages show when there is an error
)