import os
import json
import whisper

model = whisper.load_model("small")

# ✅ make sure output folder exists
os.makedirs("jsons", exist_ok=True)

audios = os.listdir("audios")

for audio in audios:
    number = audio.split("_")[0]
    title = audio.split("_")[1][:-4]
    print(number, title)

    result = model.transcribe(
        audio=f"audios/{audio}",
        language="hi",
        task="translate",
        fp16=False
    )

    chunks = []
    for segment in result["segments"]:
        chunks.append({
            "start": f"{segment['start']} sec",
            "end": f"{segment['end']} sec",
            "text": segment["text"].strip()
        })
    full_text = result["text"]

    full_text_with_chunks = {
        "text": full_text,
        "chunks": chunks
    }

    # ✅ sanitize filename (remove spaces, &)
    safe_name = audio.replace(" ", "_").replace("&", "and")

    # Save chunks into a JSON file
    with open(f"jsons/{safe_name}.json", "w", encoding="utf-8") as f:
        json.dump(full_text_with_chunks, f, ensure_ascii=False, indent=4)

print("✅ All audios processed into clean JSON files!")
