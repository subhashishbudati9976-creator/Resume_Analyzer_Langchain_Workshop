from google import genai

from config import GEMINI_API_KEY, MODEL_NAME


def main() -> None:
    client = genai.Client(api_key=GEMINI_API_KEY)
    interaction = client.interactions.create(
        model=MODEL_NAME,
        input="Explain Generative AI in three simple sentences for engineering students.",
    )
    print(interaction.output_text)


if __name__ == "__main__":
    main()
