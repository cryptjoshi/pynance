FROM node:12-alpine3.15

# RUN apk update & apk install yarn -y

WORKDIR /usr/src/app

COPY package*.json ./

RUN yarn install

COPY . .

EXPOSE 3000
 
CMD [ "yarn", "start" ]
