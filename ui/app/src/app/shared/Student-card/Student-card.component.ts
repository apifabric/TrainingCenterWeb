import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Student-card.component.html',
  styleUrls: ['./Student-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Student-card]': 'true'
  }
})

export class StudentCardComponent {


}