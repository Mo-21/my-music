import { factory, oneOf, primaryKey } from "@mswjs/data";
import { faker } from "@faker-js/faker";

const membershipStatuses = ["R", "P"];

export const db = factory({
  user: {
    id: primaryKey(faker.number.int),
    first_name: faker.person.firstName,
    last_name: faker.person.lastName,
    username: faker.internet.userName,
    email: faker.internet.email,
  },

  customer: {
    id: primaryKey(faker.number.int),
    phone: faker.phone.number,
    birthdate: faker.date.past,
    membership_status: () => faker.helpers.arrayElement(membershipStatuses),
    profile_image: faker.image.avatar,
    user: oneOf("user"),
  },

  post: {
    id: primaryKey(faker.number.int),
    content: faker.lorem.paragraph,
    image: faker.image.urlPicsumPhotos,
    created_at: faker.date.recent,
    author: () => {
      const user = db.user.create();
      const customer = db.customer.create({ user });
      return customer;
    },
  },
});
