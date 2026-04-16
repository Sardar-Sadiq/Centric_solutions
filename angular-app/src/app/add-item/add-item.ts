import { Component, EventEmitter, Output } from '@angular/core';
import { ReactiveFormsModule, FormControl } from '@angular/forms';
@Component({
  selector: 'app-add-item',
  imports: [ReactiveFormsModule],
  templateUrl: './add-item.html',
  styleUrl: './add-item.css',
})
export class AddItem {
  newTask = new FormControl('');
  
  @Output() newTodo = new EventEmitter<string>();

  submitTodo() {
    const task = this.newTask.value?.trim(); //this is will take the value of the i/p field and trim it to remove any leading or trailing whitespace
    if(task){
      this.newTodo.emit(task);
      console.log(task);
      this.newTask.setValue('');
    }    

  }
}

// what happening here is we have created a form control called newTask which will be binded to the input field in the template. We have also created an output event emitter called newTodo which will emit the new task to the parent component when the submit button is clicked. The submitTodo method will check if the task is not empty and then emit the task and reset the input field.