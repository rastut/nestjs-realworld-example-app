FROM node:12.22.6-buster-slim  as builder
WORKDIR /usr/src/app
COPY package.json yarn.lock ./
RUN npm install

FROM node:12.22.6-buster-slim as local
WORKDIR /usr/src/app
COPY . .
COPY --from=builder /usr/src/app/node_modules ./node_modules
EXPOSE 3000
