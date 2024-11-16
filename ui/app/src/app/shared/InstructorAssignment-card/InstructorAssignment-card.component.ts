import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './InstructorAssignment-card.component.html',
  styleUrls: ['./InstructorAssignment-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.InstructorAssignment-card]': 'true'
  }
})

export class InstructorAssignmentCardComponent {


}