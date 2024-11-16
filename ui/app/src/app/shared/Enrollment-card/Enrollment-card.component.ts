import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Enrollment-card.component.html',
  styleUrls: ['./Enrollment-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Enrollment-card]': 'true'
  }
})

export class EnrollmentCardComponent {


}