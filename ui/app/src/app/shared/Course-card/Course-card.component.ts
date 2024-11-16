import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Course-card.component.html',
  styleUrls: ['./Course-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Course-card]': 'true'
  }
})

export class CourseCardComponent {


}