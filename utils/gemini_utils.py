from google import genai
API_KEY = "YOUR API KEY HERE"

client = genai.Client(api_key=API_KEY)

def get_manim_code(concept):
    prompt = f"""
Write a complete Python script for manimgl (using manimlib, not the new manim) to visualize and explain the following math concept: {concept}.
- Use only manimlib (manimgl) classes and methods, for example: from manimlib import *.
- Do NOT use Axes.plot, do NOT use x_length/y_length arguments, and do NOT use features from the new manim.
- The code must be ready to run with 'manimgl'.
- Only output the code, no explanations.
- IMPORTANT: Do NOT use ANY Tex, MathTex, or LaTeX-based objects. Use only Text() for all text and labels, even for formulas.
- Do NOT use Create, Uncreate, TransformMatchingShapes, ReplacementTransform, or any class only available in Manim Community. Use ONLY ShowCreation, Write, FadeIn, FadeOut, Transform, ReplacementTransform, etc. as in manimlib.
- Do NOT use keyword arguments like x_label_text or y_label_text. Use only positional arguments and methods that exist in manimlib.
- Always include all necessary imports for every class or function you use (for example, from manimlib import *).
- Make sure the code is minimal, robust, and guaranteed to run without any errors on manimgl.
- If you are not sure about a class or method, do NOT use it.
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-04-17",
            contents=prompt,
        )
        manim_code = response.text
        # Nettoyage éventuel du code
        if "```python" in manim_code:
            manim_code = manim_code.split("```python")[1]
        if "```" in manim_code:
            manim_code = manim_code.split("```")[0]
        return manim_code.strip()
    except Exception as e:
        print(f"Erreur lors de la communication avec Gemini: {e}")
        from .manim_utils import generate_manim_code
        return generate_manim_code(concept)