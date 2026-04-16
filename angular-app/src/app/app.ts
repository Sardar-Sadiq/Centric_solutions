import { Component, signal } from '@angular/core';
import { AddItem } from './add-item/add-item';
import { TodoList } from './todo-list/todo-list';
@Component({
  selector: 'app-root',
  imports: [AddItem, TodoList],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('angular-app');

  todos: string[] = [];

  addTodo(newTodo: string){
    if (newTodo){
      this.todos.push(newTodo)
      console.log(this.todos);
    }
  }

  handleDeletedTodo(index: number){
    this.todos.splice(index, 1);
  }



}

//here we created the todos array which will hold the list of tasks. We also created the addTodo method which will be called when the newTodo event is emitted from the AddItem component. This method will check if the newTodo is not empty and then push it to the todos array. We also log the todos array to the console to see the updated list of tasks.
