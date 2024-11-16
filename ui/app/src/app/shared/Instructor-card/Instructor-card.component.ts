import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Instructor-card.component.html',
  styleUrls: ['./Instructor-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Instructor-card]': 'true'
  }
})

export class InstructorCardComponent {


}