FROM alpine

RUN apk add --no-cache curl

CMD ["curl", "--version"]