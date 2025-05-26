FROM python:latest

WORKDIR /osint

RUN python -m pip install --user pipx
RUN python -m pipx ensurepath
RUN git clone https://github.com/lanmaster53/recon-ng.git .
RUN pip install -r REQUIREMENTS

ENTRYPOINT [ "./recon-ng" ]
