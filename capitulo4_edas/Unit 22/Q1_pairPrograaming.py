def check_html_tags(html):
    stack = []
    i = 0
    while i < len(html):
        if html[i] == '<':
            # Detecta el final de la etiqueta
            j = i + 1
            while j < len(html) and html[j] != '>':
                j += 1
            if j == len(html):
                return False  # Etiqueta sin cerrar correctamente
            
            tag = html[i+1:j]
            if not tag.startswith('/'):
                # Etiqueta de apertura
                stack.append(tag.strip())
            else:
                # Etiqueta de cierre
                closing_tag = tag[1:].strip()
                if not stack or stack[-1] != closing_tag:
                    return False
                stack.pop()
            i = j
        i += 1
    return len(stack) == 0


# Ejemplo de uso:
html_code = """
<html>
<body>
<h1>Hello, World!</h1>
<p>We are learning the art of coding with Python programming language. Here we are learning ... </p>
<ul>
<li>Data Structures,</li>
<li>Algorithms,</li>
<li>and Computational Thinking, eventually.</li>
</ul>
</body>
</html>
"""

print(check_html_tags(html_code))  # Output: True
