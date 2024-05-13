import os
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4o",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)


res = llm.invoke(
    [
        HumanMessage(
            content=[
                {"type": "text", "text": "¿Qué ves en la imagen?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://i.ytimg.com/vi/P2ObevJxCoo/maxresdefault.jpg"
                    },
                },
            ]
        )
    ]
)

print(res.content)


# Output:
# En la imagen se ve una escena de una película o serie de fantasía épica. En primer plano, hay un hombre con una expresión facial intensa, que
# parece estar gritando o dando órdenes. Detrás de él, hay soldados con armaduras doradas y cascos elaborados, alineados en formación militar.
# El ambiente sugiere que están en un campo de batalla o en una preparación para una batalla. La iluminación y la estética de la escena indican
# que es una producción de alta calidad.