FROM duckietown/dt-duckiebot-interface:daffy-arm32v7

WORKDIR /duckietown_color_detector

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY color_detector.py .

CMD python3 ./color_detector.py
