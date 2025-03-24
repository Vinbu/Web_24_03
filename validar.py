import rutpy

def validate(rut : str) -> bool:
    return rutpy.validate(rut)

if __name__== "__main__":
    rut = "123546578-9"
    print(validate(ruts))