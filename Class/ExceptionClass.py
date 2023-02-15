class LessColumns(Exception):
    def __init__(self):
       print("you input has non efficient number of columns")
    pass

class MissingName(Exception):
   def __init__(self):
       print("warning, you program has no program name")
   pass

class InvalidInstruction(Exception):
    def __init__(self):
       print("ERROR, invalid instruction")
    pass

class LongerName(Exception):
   def __init__(self):
       print("warning, you program has long program name")
   pass