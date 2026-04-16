import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-todo-list',
  imports: [],
  templateUrl: './todo-list.html',
  styleUrl: './todo-list.css',
})
export class TodoList {

  @Input() TodoList: string[] = [];

  @Output() todoDeleted = new EventEmitter<number>();

  delete(index: number){
    this.todoDeleted.emit(index);
  }
}



// here we ahve the input and output properties. The input property is used to receive the list of tasks from the parent component and the output property is used to emit the index of the task that is deleted. We will implement the delete functionality in the template file.