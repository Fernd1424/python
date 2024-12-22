def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

# Llama a la función y usa print para mostrar el resultado:
print(http_error(404))  # Esto debería imprimir: "Not found"