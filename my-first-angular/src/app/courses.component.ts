import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
    selector: 'courses',  //<courses></courses>
    standalone: true,
    imports: [CommonModule],
    template: `
        <section class="m-4 ">
                <h2>{{title}}</h2>
                <ul>
                <li *ngFor="let course of courses">
                {{course}}
                </li>
                </ul>
                <button class="bg-red-500 p-2 rounded-lg ">ADD</button>
        </section>
    `
})    

export class CoursesComponent {
    title = "The List of Courses";
    courses = ["Angular", "React", "Vue", "NextJS"];
    
}