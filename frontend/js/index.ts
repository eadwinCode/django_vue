import message from './message'
interface IUser {
    name: string,
    age: number
}

console.log(message)

class User implements IUser{
    constructor(user:IUser){
        this.name = user.name
        this.age = user.age
    }
    name: string    
    age: number

    get_name = () => {
        return this.name
    };
}

const Peter = new User({name:'Peter', age:32})
console.log(Peter)