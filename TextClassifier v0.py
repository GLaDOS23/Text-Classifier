import tensorflow as tf
from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

data = "0| Формула: a^2 + b^2 = c^2 / 1| Определение: Треугольник - это геометрическая фигура с тремя сторонами./ 2| Пояснение: В данной задаче используется теорема Пифагора."

segments = data.split("/")

labels, texts = [], []
for segment in segments:
    label, text = segment.split("|")
    labels.append(label)
    texts.append(text)
tokenized_texts = [tokenizer.encode(text) for text in texts]


#input_ids = tf.convert_to_tensor(tokenized_texts, dtype=tf.int32)
input_ids = tf.ragged.constant(tokenized_texts, dtype=tf.int32)
labels = [int(label) for label in labels]
labels = tf.convert_to_tensor(labels, dtype=tf.int32)
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(tokenizer.vocab_size, 128),
    tf.keras.layers.LSTM(128, return_sequences=True),
    tf.keras.layers.LSTM(128),
     tf.keras.layers.Dense(tf.size(tf.unique(labels)), activation="softmax")
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(input_ids, labels, epochs=10)

new_text = "Формула: a^2 + b^2 = c^2"
new_tokens = tokenizer.encode(new_text)
new_input_ids = tf.convert_to_tensor([new_tokens], dtype=tf.int32)
predicted_label = model.predict(new_input_ids).argmax()
print("Ответ:", labels[predicted_label])
