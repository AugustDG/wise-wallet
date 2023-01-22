FROM node:16-alpine

COPY package.json /home/node/app/package.json
COPY build/ /home/node/app/

EXPOSE 3000

CMD ["node", "/home/node/app/index.js"]